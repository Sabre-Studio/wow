package BlizzApi

// https://us.api.blizzard.com/data/wow/connected-realm/60?namespace=dynamic-us

type AutoGenerated struct {
	Links              Links              `json:"_links"`
	ID                 int                `json:"id"`
	HasQueue           bool               `json:"has_queue"`
	Status             Status             `json:"status"`
	Population         Population         `json:"population"`
	Realms             []Realms           `json:"realms"`
	MythicLeaderboards MythicLeaderboards `json:"mythic_leaderboards"`
	Auctions           Auctions           `json:"auctions"`
}
type Self struct {
	Href string `json:"href"`
}
type Links struct {
	Self Self `json:"self"`
}
type Name struct {
	EnUS string `json:"en_US"`
	EsMX string `json:"es_MX"`
	PtBR string `json:"pt_BR"`
	DeDE string `json:"de_DE"`
	EnGB string `json:"en_GB"`
	EsES string `json:"es_ES"`
	FrFR string `json:"fr_FR"`
	ItIT string `json:"it_IT"`
	RuRU string `json:"ru_RU"`
	KoKR string `json:"ko_KR"`
	ZhTW string `json:"zh_TW"`
	ZhCN string `json:"zh_CN"`
}
type Status struct {
	Type string `json:"type"`
	Name Name   `json:"name"`
}
type Population struct {
	Type string `json:"type"`
	Name Name   `json:"name"`
}
type Key struct {
	Href string `json:"href"`
}
type Region struct {
	Key  Key  `json:"key"`
	Name Name `json:"name"`
	ID   int  `json:"id"`
}
type ConnectedRealm struct {
	Href string `json:"href"`
}
type Category struct {
	EnUS string `json:"en_US"`
	EsMX string `json:"es_MX"`
	PtBR string `json:"pt_BR"`
	DeDE string `json:"de_DE"`
	EnGB string `json:"en_GB"`
	EsES string `json:"es_ES"`
	FrFR string `json:"fr_FR"`
	ItIT string `json:"it_IT"`
	RuRU string `json:"ru_RU"`
	KoKR string `json:"ko_KR"`
	ZhTW string `json:"zh_TW"`
	ZhCN string `json:"zh_CN"`
}
type Type struct {
	Type string `json:"type"`
	Name Name   `json:"name"`
}
type Realms struct {
	ID             int            `json:"id"`
	Region         Region         `json:"region"`
	ConnectedRealm ConnectedRealm `json:"connected_realm"`
	Name           Name           `json:"name"`
	Category       Category       `json:"category"`
	Locale         string         `json:"locale"`
	Timezone       string         `json:"timezone"`
	Type           Type           `json:"type"`
	IsTournament   bool           `json:"is_tournament"`
	Slug           string         `json:"slug"`
}
type MythicLeaderboards struct {
	Href string `json:"href"`
}
type Auctions struct {
	Href string `json:"href"`
}
