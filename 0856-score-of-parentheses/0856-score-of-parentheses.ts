
function scoreOfParentheses(s: string): number {
    let scores = [0]
    for (const c of s) {
        if (c == '(') {
            scores.push(0);
        } else {
            const last = scores.pop();
            scores[scores.length - 1] += (last == 0) ? 1 : last * 2;
        }
    }
    return scores.pop();
};