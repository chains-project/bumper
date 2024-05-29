Here is a possible patch for the given code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
In this patch, I replaced the `getClassInfo` method with the `getClassInfoFor` method, which was added in a later version of the `CoverageDatabase` class. This method takes a single `ClassName` argument instead of a `Set<ClassName>`, which is consistent with the argument of the original `getClassInfo` method. I assume that this new method does the same thing as the old one, at least for the purpose of this code.