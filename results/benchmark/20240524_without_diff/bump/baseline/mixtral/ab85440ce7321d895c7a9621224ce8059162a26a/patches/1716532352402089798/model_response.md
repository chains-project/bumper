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

In the new library version, the `StringContains` constructor has been changed, and now it only accepts a single `String` argument. I replaced it with the `StringStartsWith` matcher, which checks if the provided `String` starts with the specified substring.