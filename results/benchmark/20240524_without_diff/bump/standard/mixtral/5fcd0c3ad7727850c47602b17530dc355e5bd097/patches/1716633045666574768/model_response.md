Here is a possible patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, we replaced the `getClassInfo` method with the `getClassInfoFor` method, which was added in a later version of the library. This method takes a single `ClassName` argument instead of a `Set<ClassName>`. We assume that the `data.getMutatedClass()` method returns a single `ClassName` object, which can be passed directly to the `getClassInfoFor` method.