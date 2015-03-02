package com.powerje.interviews;

import java.util.ArrayList;
import java.util.List;

public final class Combos {
    public static void main(String[] input) {
        System.out.println(Combos.replaceQuestionMarks("1?1??"));
    }

    private static List<String> replaceQuestionMarks(String input) {
        int pos = input.indexOf('?');
        if (pos == -1) {
            List<String> list = new ArrayList<String>();
            list.add(input);
            return list;
        }

        List<String> res1 = replaceQuestionMarks(Combos.replaceCharAt(input, pos, '0'));
        List<String> res2 = replaceQuestionMarks(Combos.replaceCharAt(input, pos, '1'));
        res1.addAll(res2);
        return res1;
    }

    public static String replaceCharAt(String s, int pos, char c) {
        return s.substring(0, pos) + c + s.substring(pos + 1);
    }
}
