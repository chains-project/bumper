Here's the updated `largeImageUploadWorks` method that should fix the error:

```java
@Test
void largeImageUploadWorks() throws Exception {
    try {
        this.buildImage();
        final String output = this.client.run("push", this.remote());
        MatcherAssert.assertThat(output, new StringContains("Pushed"));
    } finally {
        this.client.run("rmi", this.remote());
    }
}
```

The only change I made is to remove the `false` argument from the `StringContains` constructor. It seems like the constructor signature has changed in the new library version, and it no longer accepts a boolean argument.