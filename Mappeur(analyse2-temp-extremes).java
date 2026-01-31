cat > Mappeur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mappeur extends Mapper<LongWritable, Text, Text, Text> {
    
    private Text etat = new Text();
    private Text temperatures = new Text();
    
    @Override
    public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
        
        if (key.get() == 0) return;
        
        String ligne = value.toString();
        String[] colonnes = ligne.split("\",\"");
        
        if (colonnes.length >= 12) {
            try {
                String nomEtat = colonnes[8].replace("\"", "").trim();
                String tempMax = colonnes[10].replace("\"", "").trim();
                String tempMin = colonnes[11].replace("\"", "").trim();
                
                etat.set(nomEtat);
                temperatures.set(tempMax + "," + tempMin);
                context.write(etat, temperatures);
            } catch (Exception e) {
            }
        }
    }
}
EOF