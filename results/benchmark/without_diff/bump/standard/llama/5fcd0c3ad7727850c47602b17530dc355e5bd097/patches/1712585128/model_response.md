Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass().getName())));
}
```
The change is in the last argument of the `getClassInfo` method, which now passes `java.util.Collections.singleton(data.getMutatedClass().getName())` instead of `java.util.Collections.singleton(data.getMutatedClass())`.

The reason for this change is that the `getClassInfo` method has been removed from the `CoverageDatabase` interface, and the new method `getClassInfo(String className)` has been added. The old method signature was `getClassInfo(java.util.Set<org.pitest.classinfo.ClassName> classNames)`, which is not compatible with the new method signature.

By passing the name of the mutated class instead of the class object, we can use the new `getClassInfo(String className)` method, which returns the same information as the old method, but with a different signature. This change should fix the error and allow the code to compile again.