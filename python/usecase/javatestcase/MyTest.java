package com.test;

public class MyTest {
    public static void main(String[] args) throws Exception{
        // java -Xmx4m -classpath:./lib/*.jar com.test.MyTest userId questionId

        String userId = args[0];
        int questionId = Integer.parseInt(args[1]);

        String clz = "com.test.MyAnswer_" + userId;
        MyAnswer answer = (MyAnswer)Class.forName(clz).newInstance();
        System.setProperty("java.io.tmpdir", "/kdfjkafjdfkj");

        CPUMeasure cpu = new CPUMeasure();
        cpu.start(1);
        int MAX_ELAPSE = 2000;
        boolean correct = false;
        StringBuilder errorInfo = new StringBuilder();
        if (questionId == 1){
            MAX_ELAPSE = 2000;
            correct = isAnswer1Correct(answer, errorInfo);
        }else if (questionId == 2){
            MAX_ELAPSE = 2000;
            correct = isAnswer2Correct(answer, errorInfo);
        }else if (questionId == 3){
            MAX_ELAPSE = 5000;
            correct = isAnswer3Correct(answer, errorInfo);
        }
        cpu.end();

        long elapse = cpu.getAvgEleapseMs();
        int score = 0;
        if (correct && elapse <= MAX_ELAPSE){
            score = 20;
        }
        // output:
        // ----------##,x3131,1,RESULT_CORRECT,232ms
        // ----------##,x3131,1,20
        String fmt1 = "----------##,%s,%d,%s,%dms,%s";
        String fmt2 = "----------##,%s,%d,%d";
        String error = errorInfo.toString().replace(',', ' ');
        System.out.println(String.format(fmt1, userId, questionId, correct?"RESULT_CORRECT":"RESULT_WRONG",elapse, error));
        System.out.println(String.format(fmt2, userId, questionId, score));
    }

    private static boolean isAnswer1Correct(MyAnswer answer, StringBuilder outputErrorInfo){
        try{
            int result = answer.test1();
            return result == 31;
        }catch (Throwable t){
            outputErrorInfo.append("exception " + t.getClass() + "," + t.getMessage());
            return false;
        }
    }

    private static boolean isAnswer2Correct(MyAnswer answer, StringBuilder outputErrorInfo){
        try{
            int result = answer.test2();
            return result == 32;
        }catch (Throwable t){
            outputErrorInfo.append("exception " + t.getClass() + "," + t.getMessage());
            return false;
        }
    }

    private static boolean isAnswer3Correct(MyAnswer answer, StringBuilder outputErrorInfo){
        try{
            int result = answer.test3();
            return result == 33;
        }catch (Throwable t){
            outputErrorInfo.append("exception " + t.getClass() + ":" + t.getMessage());
            return false;
        }
    }
}
