Here is a possible patch for the code you provided:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was added in a later version of the library and should be available in your version. This method takes a single `ClassName` object as an argument, rather than a set of `ClassName` objects, which is why I was able to remove the `Collections.singleton` method call.