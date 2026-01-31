cat > Reducteur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducteur extends Reducer<Text, Text, Text, Text> {
    
    @Override
    public void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        
        int maxTemp = Integer.MIN_VALUE;
        int minTemp = Integer.MAX_VALUE;
        
        for (Text val : values) {
            String[] temps = val.toString().split(",");
            try {
                int max = Integer.parseInt(temps[0]);
                int min = Integer.parseInt(temps[1]);
                
                if (max > maxTemp) maxTemp = max;
                if (min < minTemp) minTemp = min;
            } catch (Exception e) {
            }
        }
        
        context.write(key, new Text("Max=" + maxTemp + ", Min=" + minTemp));
    }
}
EOF