Here is the proposed patch for the failing client code:

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

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only requires a single argument. This should resolve the error message about the constructor having the wrong number of arguments.