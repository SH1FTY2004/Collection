# Deníček projektu – Uživatelské kolekce (`gql_metadata/Collections`)

**Autoři:** Pavlis Lukáš a Nikola Haluzová

Tento dokument je deník celého průběhu vývoje projektu od prvního commitu až po stav před závěrečnou obhajobou. Zachycuje časovou posloupnost commitů, problémy, které jsme si definovali k vyřešení, co jsme při tom objevili, a hlavně které problémy se dlouho nedařilo řešit a jak byly nakonec vyřešeny.

## Definice problému – co má aplikace umět

Tématem projektu je systém uživatelských kolekcí, do kterých lze ukládat libovolné entity informačního systému (například projekty, grantové výzvy nebo dokumenty). Zadání jsme si na začátku semestru definovali takto:

* `CollectionGQLModel` (kolekce) = pojmenovaná kolekce uživatele, například „Oblíbené", „Projekty k projednání", „Dokumenty k přečtení" nebo „Zajímavé grantové výzvy". Má název (`name`), popis (`description`), vlastníka (`owner_id`) a barvu (`color`).
* `CollectionItemGQLModel` (položka kolekce) = jedna vložená entita. Odkazuje na kolekci (`collection_id`), na vloženou entitu (`entity_id`) a její typ (`entity_type_id`), má svého vlastníka (`owner_id`) a pořadí v kolekci (`position`).
* Jedna kolekce může obsahovat entity různých typů, například kolekce „Oblíbené" může obsahovat 1. Project A, 2. Grant B, 3. Document C.
* Odkaz na vloženou entitu je polymorfní: dvojice `entity_id` + `entity_type_id` místo klasického cizího klíče.
* Z hlediska editace musím být schopen kolekci vytvořit, upravit a smazat a v ní položky přidávat, odebírat a řadit.
* Důležité: kolekce jen odkazuje na entity, nekopíruje je. Položka kolekce není vložená entita samotná.

Z toho vyplynuly hlavní problémy k vyřešení:

1. Vytvořit databázové modely `Collection` a `CollectionItem` a číselník typů entit implementovaný jako strom (typy typů).
2. Umožnit vytváření, úpravu a mazání kolekcí pomocí GraphQL mutací.
3. Umožnit přidávat a odebírat položky kolekce.
4. Umožnit řadit položky v kolekci (udržovat správně `position` při vkládání, odebírání a přesunu).
5. Rozhodnout, jak ošetřit polymorfní referenci (ověřovat existenci vložené entity, nebo ne).
6. Vyřešit autorizaci: kdo smí kolekci číst a měnit a jak naložit s `owner_id` u položky.
