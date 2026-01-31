cat > Reducteur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducteur extends Reducer<Text, Text, Text, Text> {
    
    @Override
    public void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        
        double sommeTemp = 0.0;
        double sommePrecip = 0.0;
        int compte = 0;
        
        for (Text val : values) {
            String[] parts = val.toString().split(",");
            try {
                sommeTemp += Double.parseDouble(parts[0]);
                sommePrecip += Double.parseDouble(parts[1]);
                compte++;
            } catch (Exception e) {
            }
        }
        
        double moyTemp = sommeTemp / compte;
        double moyPrecip = sommePrecip / compte;
        
        String resultat = String.format("Temp_moy=%.2f, Precip_tot=%.2f, Precip_moy=%.2f", 
                                        moyTemp, sommePrecip, moyPrecip);
        
        context.write(key, new Text(resultat));
    }
}
EOF