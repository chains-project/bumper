Here's the fixed version of the `shouldPush` method:

```java
@Test
void shouldPush() throws Exception {
    final Image original = new Image.ForOs();
    final String image = this.copy(original);
    final String output = this.cli.run("push", image);
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("latest: digest: %s", original.digest())
        )
    );
}
```

The change is in the `assertThat` statement. The `StringContains` matcher has been replaced with the `StringStartsWith` matcher, which only takes a single argument - the expected prefix. This resolves the error message about the constructor of `StringContains` not accepting two arguments.