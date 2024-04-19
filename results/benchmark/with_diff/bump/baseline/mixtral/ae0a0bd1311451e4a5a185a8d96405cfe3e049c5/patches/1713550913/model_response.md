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
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", image)
        )
    );
}
```

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which has the same first argument type as the failed constructor. This change makes the code compatible with the new library version.