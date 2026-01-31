cat > Mappeur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mappeur extends Mapper<LongWritable, Text, Text, IntWritable> {
    
    private Text etat = new Text();
    private IntWritable temperature = new IntWritable();
    
    @Override
    public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
        
        if (key.get() == 0) return;
        
        String ligne = value.toString();
        String[] colonnes = ligne.split("\",\"");
        
        if (colonnes.length >= 11) {
            try {
                String nomEtat = colonnes[8].replace("\"", "").trim();
                String tempStr = colonnes[9].replace("\"", "").trim();
                int tempMoyenne = Integer.parseInt(tempStr);
                
                etat.set(nomEtat);
                temperature.set(tempMoyenne);
                context.write(etat, temperature);
            } catch (Exception e) {
            }
        }
    }
}
EOF
javac -classpath $HADOOP_CLASSPATH *.java
jar -cvf analyse1.jar *.class
mv analyse1.jar ../../jars/
hdfs dfs -rm -r /user/hadoop/meteo/output/analyse1
hadoop jar ../../jars/analyse1.jar Driver /user/hadoop/meteo/input/weather.csv /user/hadoop/meteo/output/analyse1