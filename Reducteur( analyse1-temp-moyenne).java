cat > Reducteur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducteur extends Reducer<Text, IntWritable, Text, DoubleWritable> {
    
    private DoubleWritable resultat = new DoubleWritable();
    
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {
        
        int somme = 0;
        int compte = 0;
        
        for (IntWritable val : values) {
            somme += val.get();
            compte++;
        }
        
        double moyenne = (double) somme / compte;
        resultat.set(moyenne);
        
        context.write(key, resultat);
    }
}
EOF