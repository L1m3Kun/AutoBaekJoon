import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split("");
        int i =0;
        int cnt = 0;
        while(i<str.length){
            if(str[i].equals("c")){
                if(i+1 >= str.length){
                    cnt ++;
                    i++;
                }
                else if(str[i+1].equals("=")){
                    cnt ++;
                    i += 2;
                }
                else if(str[i+1].equals("-")){
                    cnt ++;
                    i += 2;
                }
                else {
                    cnt ++;
                    i ++;
                }
            }
            else if(str[i].equals("d")){
                if(i+1 >= str.length){
                    cnt ++;
                    i ++;
                }
                else if(str[i+1].equals("-")){
                    cnt ++;
                    i +=2;
                }
                else if(i+2 >= str.length){
                    cnt ++;
                    i++;
                }
                else if(str[i+1].equals("z")){
                    if(str[i+2].equals("=")){
                        cnt ++;
                        i+=3;
                    }
                    else{
                        cnt++;
                        i++;
                    }
                }
                else{
                    cnt ++;
                    i++;
                }

            }
            else if(str[i].equals("l")){
                if(i+1 >= str.length){
                    cnt ++;
                    break;
                }
                else if(str[i+1].equals("j")){
                    cnt ++;
                    i+=2;
                }
                else{
                    cnt ++;
                    i++;
                }
            }
            else if(str[i].equals("n")){
                if(i+1 >= str.length){
                    cnt ++;
                    i++;
                }
                else if(str[i+1].equals("j")){
                    cnt ++;
                    i+=2;
                }
                else{
                    cnt ++;
                    i++;
                }
            }
            else if(str[i].equals("s")){
                if(i+1 >= str.length){
                    cnt ++;
                    i++;
                }
                else if(str[i+1].equals("=")){
                    cnt ++;
                    i+=2;
                }
                else{
                    cnt ++;
                    i++;
                }
            }
            else if(str[i].equals("z")){
                if(i+1 >= str.length){
                    cnt ++;
                    i++;
                }
                else if(str[i+1].equals("=")){
                    cnt ++;
                    i+=2;
                }
                else{
                    cnt ++;
                    i++;
                }
            }
            else{
                cnt ++;
                i++;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}