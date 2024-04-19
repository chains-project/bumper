Here is a possible patch for the failing client code:

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

The change I made is to remove the `false` argument from the `StringContains` constructor, as it is not needed and is causing the error. The `MatcherAssert.assertThat` method will still work as expected without it.