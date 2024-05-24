Here's the proposed patch for the failing client code:

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

In the original code, the `StringContains` matcher is used with two arguments, which is not valid in the new library version. Instead, I used the `StringStartsWith` matcher, which takes a single argument and checks if the input string starts with the given substring. This should fix the error and make the test pass.