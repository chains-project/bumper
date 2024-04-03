Here is a possible patch for the code you provided:

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

The only change I made is to remove the `false` argument from the `StringContains` constructor. It looks like the `StringContains` constructor in the new library version no longer accepts a `boolean` argument, so I removed it to make the code compatible with the new library version.

I hope this helps! Let me know if you have any questions.