import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str;
        int maxV, x, y;
        maxV = -1;
        x = 0;
        y = 0;
        for(int i=0;i<9;i++){
            str = br.readLine().split(" ");
            for(int j=0;j<9;j++){
                if(Integer.parseInt(str[j]) > maxV){
                    x = i+1;
                    y = j+1;
                    maxV = Integer.parseInt(str[j]);
                }
            }
        }
        bw.write(String.valueOf(maxV));
        bw.newLine();
        bw.write(String.valueOf(x+" "+y));
        bw.flush();
    }
}