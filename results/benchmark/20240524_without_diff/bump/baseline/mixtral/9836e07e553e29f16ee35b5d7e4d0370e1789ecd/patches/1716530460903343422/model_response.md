Here's a possible patch for the failing client code:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(String.format("Status: Downloaded newer image for %s", image))
    );
}
```

The change I made is to remove the `false` argument in the `StringContains` constructor. The error message indicates that the constructor expects only one argument, which is a string, but it's receiving two arguments instead. The `false` argument was likely added by mistake and is not needed.