/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ws4j;

import edu.cmu.lti.lexical_db.ILexicalDatabase;
import edu.cmu.lti.lexical_db.NictWordNet;
import edu.cmu.lti.ws4j.impl.Lin;
import edu.cmu.lti.ws4j.impl.Path;
import edu.cmu.lti.ws4j.impl.WuPalmer;
import edu.cmu.lti.ws4j.util.WS4JConfiguration;
import java.util.Collections;
import java.util.PriorityQueue;

/**
 *
 * @author jason
 */
public class WS4J {

    private static ILexicalDatabase db = new NictWordNet(); 
    private static double computeWUP (String word1, String word2) {
        WS4JConfiguration.getInstance().setMFS(true);
        double s = new WuPalmer(db).calcRelatednessOfWords(word1, word2);
        return s;
    }
    
    private static double computeLin(String w1, String w2) {
        WS4JConfiguration.getInstance().setMFS(true);
        double s = new Path(db).calcRelatednessOfWords(w1, w2);
        return s;
    }
  
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        System.out.println("Relatedness: " + computeWUP("yeast", "bread"));
        long end = System.currentTimeMillis();
        System.out.println(end - start);
        
        
        // mess with priority queue
        PriorityQueue<Integer> pq = new PriorityQueue<>( Collections.reverseOrder());
        pq.add(5);
        pq.offer(3);
        pq.offer(10);
        pq.add(309);
        pq.offer(1);
        
        while (pq.peek() != null) {
            System.out.println(pq.poll());
        }
    }
    
    
    
}
