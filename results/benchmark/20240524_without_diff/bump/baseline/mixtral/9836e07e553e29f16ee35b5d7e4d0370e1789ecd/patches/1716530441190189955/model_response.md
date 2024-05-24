Here is a possible patch for the failing code:
```java
@Test
void shouldPull() throws Exception {
    final String image = this.copy(new Image.ForOs());
    this.cli.run("push", image);
    this.cli.run("image", "rm", image);
    final String output = this.cli.run("pull", image);
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```
The change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher. This is because the `StringContains` constructor that takes a `boolean` and a `String` has been removed in the new library version. Instead, the `StringStartsWith` matcher can be used to check if a string starts with a given substring.

Note that I did not need to create any new variables or remove the `@Override` decorator. I also did not use any removed library methods or change the function signature. I only changed the matcher used in the `assertThat` statement.