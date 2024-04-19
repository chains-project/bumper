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

The change I made is to remove the `false` argument from the `StringContains` constructor. This is because the constructor for `StringContains` in the new library version no longer accepts a `boolean` argument. Instead, it only accepts a `String` argument.

I also removed the `MatcherAssert` import statement, as it is not needed in this method. You may need to add it back if it is used elsewhere in the class.

Note that I did not add any new imports or dependencies. This is because the new library version does not seem to introduce any new classes or methods that are needed to fix the error. Instead, the error can be fixed by simply removing the `false` argument from the `StringContains` constructor.