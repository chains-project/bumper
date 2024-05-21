Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the method `getClassInfo` with the method `getClassInfoFor`, which was added in a later version of the library. This method takes a single `ClassName` argument instead of a `Set<ClassName>`, which is more appropriate for the use case in the client code.