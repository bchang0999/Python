/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expect1 = true;

const str2 = "N(0(p)3";
const expect2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expect3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expect4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    counter = 0
    for (var i = 0; i < str.length; i++) {
        if ((counter >= 0) && (str[i] == '(')) {
            counter++
        }
        else if ((counter >= 0)&& (str[i] == ')')) {
            counter--
        }{
        if (counter < 0){
            return false}
    }
    }
    if (counter != 0){
        return false
    } return true
    }

console.log (parensValid(str1))
/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1a = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2a = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3a = "A(1)(s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var counter = 0
    var x = 0
    var y = 0
    for (var i = 0; i < str.length; i++) {
        if ((counter >= 0) && (str[i] == '(')) {
            counter++
        }
        if ((counter >= 0) && (str[i] == '{')) {
            x++
        }
        if ((counter >= 0) && (str[i] == '[')) {
            y++
        }
        if ((counter >= 0)&& (str[i] == ')')) {
            counter--
        }
        if ((counter >= 0)&& (str[i] == '}')) {
            x--
        }
        if ((counter >= 0)&& (str[i] == ']')) {
            y--
        }
        {
        if (counter < 0||x <0 || y<0){
            return false}
            
    }
    console.log (counter)
    }
    if (counter != 0||x !=0 || y !=0){
        return false} return true
    }
    console.log (bracesValid(str1a))
    console.log (bracesValid(str2a))
    console.log (bracesValid(str3a))
    