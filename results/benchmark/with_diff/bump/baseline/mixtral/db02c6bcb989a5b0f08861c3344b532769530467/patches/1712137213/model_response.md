Sure, here's a possible patch for the failing client code:
```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("latest: digest: %s", original.digest())
        )
    );
}
```
In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only checks if a string starts with a given substring. This should fix the error message you were seeing, which was caused by the fact that the `StringContains` constructor now requires only one argument, instead of two.

Note that I made this change based on the assumption that the rest of the code is working correctly and that the output of the `cli.run` method contains the digest of the original image at the beginning of the string. If this is not the case, you may need to adjust the patch accordingly.