Here is a proposed patch for the failing client code:

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

The only change I made is to remove the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor in the new library version no longer accepts a `boolean` argument. Instead, it only accepts a `String` argument.

I hope this helps! Let me know if you have any questions.