Here's a possible patch for the given code:

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

The change I made is to remove the `false` argument from the `StringContains` constructor. This is because the constructor signature has changed in the new library version and no longer accepts a `boolean` argument. Instead, it only accepts a `String` argument which is the expected substring to search for in the input string.