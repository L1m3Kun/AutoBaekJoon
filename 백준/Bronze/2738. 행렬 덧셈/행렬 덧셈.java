// 2738번 행렬덧셈
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[][] str1 = new String[N][M];
        String[][] str2 = new String[N][M];
        String[] input;
        for(int i=0;i<N;i++){
            input = br.readLine().split(" ");
            for(int j=0;j<M;j++){
                str1[i][j] = input[j];
            }
        }
        for(int i=0;i<N;i++){
            input = br.readLine().split(" ");
            for(int j=0;j<M;j++){
                str2[i][j] = input[j];
            }
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                bw.write(String.valueOf(Integer.parseInt(str1[i][j]) + Integer.parseInt(str2[i][j])));
                bw.write(String.valueOf(" "));
            }
            bw.newLine();
        }
        bw.flush();
    }
}