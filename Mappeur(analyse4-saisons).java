cat > Mappeur.java << 'EOF'
import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mappeur extends Mapper<LongWritable, Text, Text, Text> {
    
    private Text saison = new Text();
    private Text donnees = new Text();
    
    @Override
    public void map(LongWritable key, Text value, Context context) 
            throws IOException, InterruptedException {
        
        if (key.get() == 0) return;
        
        String ligne = value.toString();
        String[] colonnes = ligne.split("\",\"");
        
        if (colonnes.length >= 11) {
            try {
                String precipStr = colonnes[0].replace("\"", "").trim();
                String moisStr = colonnes[2].replace("\"", "").trim();
                String tempStr = colonnes[9].replace("\"", "").trim();
                
                int mois = Integer.parseInt(moisStr);
                double precip = Double.parseDouble(precipStr);
                int temp = Integer.parseInt(tempStr);
                
                String saisonNom;
                if (mois == 12 || mois == 1 || mois == 2) saisonNom = "Hiver";
                else if (mois >= 3 && mois <= 5) saisonNom = "Printemps";
                else if (mois >= 6 && mois <= 8) saisonNom = "Ete";
                else saisonNom = "Automne";
                
                saison.set(saisonNom);
                donnees.set(temp + "," + precip);
                context.write(saison, donnees);
            } catch (Exception e) {
            }
        }
    }
}
EOF