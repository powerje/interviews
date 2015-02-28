public final class Combos {
    private static List<String> replaceQuestionMarks(String input) {
        int pos = input.indexOf('?');
        if (pos == -1) {
            return new List<String>(); 
        }

        List<String> res1 = replaceQuestionMarks(input.replaceCharAt(pos, '0'));
        List<String> res2 = replaceQuestionMarks(input.replaceCharAt(pos, '1'));
        return res1.append(res2);
    }
}
