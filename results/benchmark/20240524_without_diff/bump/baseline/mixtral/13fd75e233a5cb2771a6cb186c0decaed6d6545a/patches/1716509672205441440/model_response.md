Here's a fixed version of the `shouldPullPushedByTag` method that should resolve the error:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringContains("Status: Downloaded newer image for " + this.image.remote())
    );
}
```

The issue was caused by the `StringContains` constructor being called with two arguments instead of one. I've updated the code to pass a single string argument to the `StringContains` constructor. This should resolve the error.