Here is a proposed patch for the failing code:

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

The only change I made was to replace the `StringContains` matcher with the `StringStartsWith` matcher. This is because the `StringContains` constructor that takes a `boolean` and a `String` has been removed in the new library version, and the `StringStartsWith` matcher is a suitable alternative.

I also removed the `false` argument from the `StringStartsWith` constructor, as it is not needed in this case. The `StringStartsWith` matcher will simply check if the `output` string starts with the specified string (i.e., the expected log message).

I hope this helps! Let me know if you have any questions.