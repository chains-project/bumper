Here is a possible patch for the code you provided:
```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(original.digest())
    );
}
```
The change I made is to remove the `false` argument from the `StringContains` constructor. This argument was causing the error message you saw, because the `StringContains` constructor does not expect a boolean argument.

I also removed the `String.format` method call, because it is not necessary here. The `StringContains` constructor can take a plain string as an argument, so there is no need to format the string first.

I hope this helps! Let me know if you have any questions.