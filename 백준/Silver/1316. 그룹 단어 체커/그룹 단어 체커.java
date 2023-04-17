import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Set;
import java.util.HashSet;
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int cnt =0;
        String[] str;
        Set<String> set = new HashSet<>();
        for(int i=0;i<N;i++){
            str = br.readLine().split("");
            if(str.length == 1){
                cnt ++;
                continue;
            }
            set.clear();
            set.add(str[0]);
            for(int j=1;j<str.length;j++){
                if(!str[j].equals(str[j-1]) && set.contains(str[j])){
                    break;
                }
                set.add(str[j]);
                if(j == str.length-1){
                    cnt ++;
                }
            }

        }
        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}