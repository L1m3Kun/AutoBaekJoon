import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Map<Integer, Integer> hash = new HashMap<>();
        int N = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        int check = 0;
        int num, diff;
        for(int i=0;i<N;i++){
            num = Integer.parseInt(str[i]);
            hash.put(num, i);
            check += num;
        }
        if(check == 0) bw.write(String.valueOf(N));
        else{
            int cnt = 0;
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    diff = Integer.parseInt(str[i]) - Integer.parseInt(str[j]);
                    if(i!=j && hash.containsKey(diff) && hash.get(diff) != j && hash.get(diff) != i ){
                        cnt ++;
                        break;
                    }
                }
            }
            bw.write(String.valueOf(cnt));
        }
        bw.flush();
    }
}