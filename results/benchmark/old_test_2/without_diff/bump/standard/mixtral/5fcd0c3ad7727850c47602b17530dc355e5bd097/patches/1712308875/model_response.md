Here is a potential patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was added in a later version of the library. This method takes a single `ClassName` argument instead of a set of `ClassName`s, which should be compatible with the `getMutatedClass` method of `ClassMutationResults`.