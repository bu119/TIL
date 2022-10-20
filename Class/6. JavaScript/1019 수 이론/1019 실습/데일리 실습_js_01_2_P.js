function palindrome(str) {
    //

    str = str.toLowerCase();
    let len = str.length;
    
    for (let i = 0; i < Math.floor(len / 2); i++) {
      if (str[i] !== str[len-i-1]) return "false";
    }
    return "true";
}
  
  // 출력
  // palindrome('level') => true
  let str1="level";
  console.log(palindrome(str1));
  // palindrome('hi') => false
  let str2="hi";
  console.log(palindrome(str2));
