cat > Mappeur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mappeur extends Mapper<LongWritable, Text, Text, DoubleWritable> {
    
    private Text mois = new Text();
    private DoubleWritable precipitation = new DoubleWritable();
    
    @Override
    public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
        
        if (key.get() == 0) return;
        
        String ligne = value.toString();
        String[] colonnes = ligne.split("\",\"");
        
        if (colonnes.length >= 3) {
            try {
                String precipStr = colonnes[0].replace("\"", "").trim();
                String moisStr = colonnes[2].replace("\"", "").trim();
                
                double precip = Double.parseDouble(precipStr);
                
                mois.set("Mois_" + moisStr);
                precipitation.set(precip);
                context.write(mois, precipitation);
            } catch (Exception e) {
            }
        }
    }
}
EOF