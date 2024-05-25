Here is a fixed version of the code:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new StringContains("Status: Downloaded newer image for " + image)
    );
}
```

The issue was with the way the `StringContains` matcher was being called. Instead of passing `false` as the first argument, you should pass the expected string as a single argument. I have concatenated the expected string using the `+` operator.