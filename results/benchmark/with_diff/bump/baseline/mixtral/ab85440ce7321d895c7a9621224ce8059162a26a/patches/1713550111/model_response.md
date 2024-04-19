Here's a fixed version of the method that should work with the new library version:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", this.image.remote())
        )
    );
}
```

The only change made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which has a compatible constructor signature. This should allow the test to pass with the new library version.