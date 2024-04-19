Here's a possible patch for the failing code:

```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new StringContains(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

The change I made is to remove the `false` argument from the `new StringContains` constructor, as it is not needed and is causing the error message. The `StringContains` matcher only takes a single argument, which is the expected substring to be found in the actual string.