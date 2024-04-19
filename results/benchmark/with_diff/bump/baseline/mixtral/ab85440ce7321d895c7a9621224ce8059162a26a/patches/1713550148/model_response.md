Here's a fixed version of the `shouldPullPushedByTag` method that should resolve the error:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
            output,
            new StringContains("Status: Downloaded newer image for " + this.image.remote())
    );
}
```

The issue was caused by the incorrect usage of the `StringContains` constructor. The constructor expects only a single argument, which is the expected substring. The error message indicates that the constructor was called with two arguments, a boolean and a string, instead of just a string.

To fix the issue, I removed the `false` argument from the `StringContains` constructor and concatenated the `this.image.remote()` method with the expected substring. This ensures that the `StringContains` constructor is called with a single argument, which is the expected substring.