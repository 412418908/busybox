package com.test;

public class CPUMeasure {
    private long start;
    private int loops;
    private long avgElapse;

    public void start(int loops){
        start = System.nanoTime();
        this.loops = loops;
        System.out.println("-----start measure...");
    }


    public void end(){
        long end = System.nanoTime();
        long elapse = (end - start) / 1000000;
        avgElapse = (end - start) / loops / 1000000;
        System.out.println("-----end measure, elapse=" + elapse + "ms , avg elapse=" + avgElapse + "ms");
    }

    public long getAvgEleapseMs(){
        return avgElapse;
    }
}
