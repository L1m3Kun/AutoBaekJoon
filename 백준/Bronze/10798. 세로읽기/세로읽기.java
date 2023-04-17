// 10798번 세로읽기
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[][] str = new String[5][15];
        for(int i=0;i<5;i++){
            for(int j=0;j<15;j++){
                str[i][j] = "";
            }
        }
        String[] input;
        for(int i=0;i<5;i++){
            input = br.readLine().split("");
            for(int j=0;j<input.length;j++){
                str[i][j] = input[j];
            }
        }
        for(int i=0;i<15;i++){
            for(int j=0;j<5;j++){
                bw.write(String.valueOf(str[j][i]));
            }
        }
        bw.flush();
    }
}