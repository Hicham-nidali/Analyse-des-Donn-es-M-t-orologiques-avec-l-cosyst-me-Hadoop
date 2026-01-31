cat > Reducteur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducteur extends Reducer<Text, DoubleWritable, Text, Text> {
    
    @Override
    public void reduce(Text key, Iterable<DoubleWritable> values, Context context)
            throws IOException, InterruptedException {
        
        double somme = 0.0;
        int compte = 0;
        
        for (DoubleWritable val : values) {
            somme += val.get();
            compte++;
        }
        
        double moyenne = somme / compte;
        String resultat = String.format("Total=%.2f, Moyenne=%.2f", somme, moyenne);
        
        context.write(key, new Text(resultat));
    }
}
EOF