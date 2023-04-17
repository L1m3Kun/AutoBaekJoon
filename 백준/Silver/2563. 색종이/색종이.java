import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[][] paper = new String[100][100];
        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                paper[i][j] = "0";
            }
        }
        String[] ran;
        int N = Integer.parseInt(br.readLine());
        int M,G;
        for(int i=0;i<N;i++){
            ran = br.readLine().split(" ");
            M = Integer.parseInt(ran[0])-1;
            G = Integer.parseInt(ran[1])-1;
            for(int j=99-10-G;j<99-G;j++){
                for(int k=M;k<M+10;k++){
                    paper[j][k] = "1";
                }
            }

        }
        int cnt = 0;
        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                if(paper[i][j] == "1") cnt ++;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}