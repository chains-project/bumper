Here's a fixed version of the method that should work with the new library version:

```java
@Test
void largeImagePullWorks() throws Exception {
    try {
        this.buildImage();
        this.client.run("push", this.remote());
        this.client.run("image", "rm", this.remote());
        final String output = this.client.run("pull", this.remote());
        MatcherAssert.assertThat(
            output,
            new StringStartsWith(
                String.format("Status: Downloaded newer image for %s", this.remote())
            )
        );
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```

The change is in the assertion statement, where I replaced `StringContains` with `StringStartsWith` from the new library version. This should fix the error message you were seeing.