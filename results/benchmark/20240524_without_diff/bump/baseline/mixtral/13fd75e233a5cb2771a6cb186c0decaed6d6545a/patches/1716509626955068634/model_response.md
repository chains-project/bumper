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
The change I made is to remove the `false` argument from the `StringContains` constructor, which is causing the error message. This is because the `StringContains` constructor now only takes a single `String` argument, instead of a `boolean` and a `String`. This change is consistent with the library changes you provided, where the `--` indicates a removal of the `boolean` argument from the `StringContains` constructor.