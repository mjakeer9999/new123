int hammingDist(str1,str2)
{
    int i = 0, count = 0;
    while (str1[i] != '\0') {
        if (str1[i] != str2[i])
            count++;
        i++;
    }
    return count;
}
 
// driver code
int main()
{
    str1 = "geekspractice";
    str2 = "nerdspractise";
    // function call
    count << hammingDist(str1, str2);
    return 0;
}